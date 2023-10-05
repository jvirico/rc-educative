# StatefulSets

Example:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: managed-premium-retain
provisioner: disk.csi.azure.com
parameters:
  skuName: Premium_ZRS
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

## skuName
#### Primary region redundancy
- Locally redundant storage (LRS)
- Zone-redundant storage (ZRS)

#### Secondary region redundancy
- Geo-redundant storage (GRS)
- Geo-zone-redundant storage (GZRS)

#### According to that following skuName are available in Azure
- Standard_LRS — standard locally redundant storage (LRS)
- Standard_GRS — standard geo-redundant storage (GRS)
- Standard_ZRS — standard zone redundant storage (ZRS)
- Standard_RAGRS — standard read-access geo-redundant storage (RA-GRS)
- Premium_LRS — premium locally redundant storage (LRS)
- Premium_ZRS — premium zone redundant storage (GRS)

## Resources
- https://arunksingh16.medium.com/azure-storageclass-in-azure-kubernetes-service-aks-5167c4e7682
- https://learn.microsoft.com/en-us/azure/aks/concepts-storage
